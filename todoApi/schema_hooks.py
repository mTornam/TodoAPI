def tag_djoser_endpoints(result, generator, request, public):
    # Iterate over paths in the OpenAPI schema
    for path, path_item in result['paths'].items():
        if path.startswith('/auth/users'):
            for method in path_item:
                path_item[method]['tags'] = ['Auth - Users']
        elif path.startswith('/auth/jwt'):
            for method in path_item:
                path_item[method]['tags'] = ['Auth - Jwt']
        elif path.startswith('/auth/token'):
            for method in path_item:
                path_item[method]['tags'] = ['Auth - Token']
    return result
